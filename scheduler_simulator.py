import time
import random
from collections import deque
from threading import Thread, Lock
from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime

@dataclass
class Job:
    id: str
    cpu: int
    memory: int
    duration: float
    status: str = "pending"
    node_id: str = None
    
@dataclass
class Node:
    id: str
    cpu_total: int
    memory_total: int
    cpu_used: int = 0
    memory_used: int = 0
    status: str = "healthy"
    jobs: List[str] = field(default_factory=list)
    
    def can_fit(self, job):
        return (self.cpu_total - self.cpu_used >= job.cpu and 
                self.memory_total - self.memory_used >= job.memory and
                self.status == "healthy")
    
    def allocate(self, job):
        self.cpu_used += job.cpu
        self.memory_used += job.memory
        self.jobs.append(job.id)
    
    def release(self, job):
        self.cpu_used -= job.cpu
        self.memory_used -= job.memory
        if job.id in self.jobs:
            self.jobs.remove(job.id)

class Scheduler:
    def __init__(self, algorithm="first-fit"):
        self.algorithm = algorithm
        self.nodes: Dict[str, Node] = {}
        self.jobs: Dict[str, Job] = {}
        self.job_queue = deque()
        self.lock = Lock()
        self.metrics = {
            "total_jobs": 0, "completed": 0, "failed": 0, "running": 0,
            "nodes_added": 0, "nodes_failed": 0, "reschedules": 0
        }
        self.running = True
        
        # Initialize cluster
        for i in range(3):
            self.add_node(f"node-{i+1}", cpu=4, memory=8)
    
    def add_node(self, node_id, cpu=4, memory=8):
        with self.lock:
            self.nodes[node_id] = Node(node_id, cpu, memory)
            self.metrics["nodes_added"] += 1
            print(f"✓ Node {node_id} added [CPU:{cpu}, RAM:{memory}GB]")
    
    def submit_job(self, job_id, cpu, memory, duration):
        with self.lock:
            job = Job(job_id, cpu, memory, duration)
            self.jobs[job_id] = job
            self.job_queue.append(job_id)
            self.metrics["total_jobs"] += 1
            print(f"→ Job {job_id} submitted [CPU:{cpu}, RAM:{memory}GB, Duration:{duration}s]")
    
    def schedule_jobs(self):
        with self.lock:
            while self.job_queue:
                job_id = self.job_queue[0]
                job = self.jobs[job_id]
                
                node = self._find_node(job)
                if node:
                    self.job_queue.popleft()
                    node.allocate(job)
                    job.status = "scheduled"
                    job.node_id = node.id
                    print(f"  ✓ Job {job_id} scheduled → {node.id}")
                    Thread(target=self._execute_job, args=(job_id,), daemon=True).start()
                else:
                    # Auto-scale
                    if self._should_scale():
                        new_id = f"node-{len(self.nodes)+1}"
                        self.add_node(new_id)
                    break
    
    def _find_node(self, job):
        available = [n for n in self.nodes.values() if n.can_fit(job)]
        if not available:
            return None
        
        if self.algorithm == "first-fit":
            return available[0]
        elif self.algorithm == "best-fit":
            return min(available, key=lambda n: (n.cpu_total - n.cpu_used))
        elif self.algorithm == "round-robin":
            return min(available, key=lambda n: len(n.jobs))
        return available[0]
    
    def _should_scale(self):
        return len(self.job_queue) > 2 and len(self.nodes) < 10
    
    def _execute_job(self, job_id):
        with self.lock:
            job = self.jobs[job_id]
            job.status = "running"
            self.metrics["running"] += 1
        
        print(f"  ▶ Job {job_id} running on {job.node_id}")
        time.sleep(job.duration)
        
        with self.lock:
            job.status = "completed"
            node = self.nodes.get(job.node_id)
            if node:
                node.release(job)
            self.metrics["running"] -= 1
            self.metrics["completed"] += 1
            print(f"  ✓ Job {job_id} completed")
    
    def simulate_failure(self, node_id):
        with self.lock:
            if node_id not in self.nodes:
                return
            
            node = self.nodes[node_id]
            node.status = "failed"
            self.metrics["nodes_failed"] += 1
            print(f"✗ Node {node_id} FAILED!")
            
            # Reschedule jobs
            for job_id in list(node.jobs):
                job = self.jobs[job_id]
                if job.status in ["scheduled", "running"]:
                    job.status = "pending"
                    job.node_id = None
                    self.job_queue.append(job_id)
                    self.metrics["reschedules"] += 1
                    self.metrics["running"] -= 1
                    print(f"  ↻ Job {job_id} rescheduled")
            
            node.jobs.clear()
            node.cpu_used = 0
            node.memory_used = 0
    
    def display_metrics(self):
        print("\n" + "="*60)
        print("📊 CLUSTER METRICS DASHBOARD")
        print("="*60)
        
        with self.lock:
            # Cluster status
            healthy = sum(1 for n in self.nodes.values() if n.status == "healthy")
            total_cpu = sum(n.cpu_used for n in self.nodes.values())
            total_cpu_capacity = sum(n.cpu_total for n in self.nodes.values())
            total_mem = sum(n.memory_used for n in self.nodes.values())
            total_mem_capacity = sum(n.memory_total for n in self.nodes.values())
            
            print(f"Cluster Nodes: {len(self.nodes)} (Healthy: {healthy}, Failed: {len(self.nodes)-healthy})")
            print(f"CPU Usage: {total_cpu}/{total_cpu_capacity} cores ({total_cpu*100//total_cpu_capacity if total_cpu_capacity else 0}%)")
            print(f"Memory Usage: {total_mem}/{total_mem_capacity} GB ({total_mem*100//total_mem_capacity if total_mem_capacity else 0}%)")
            print(f"\nJobs - Total: {self.metrics['total_jobs']} | Completed: {self.metrics['completed']} | Running: {self.metrics['running']} | Queued: {len(self.job_queue)}")
            print(f"Failed Jobs: {self.metrics['failed']} | Reschedules: {self.metrics['reschedules']}")
            
            print(f"\n{'Node':<12} {'Status':<10} {'CPU':<15} {'Memory':<15} {'Jobs'}")
            print("-"*60)
            for node in self.nodes.values():
                cpu_bar = f"{node.cpu_used}/{node.cpu_total}"
                mem_bar = f"{node.memory_used}/{node.memory_total}GB"
                print(f"{node.id:<12} {node.status:<10} {cpu_bar:<15} {mem_bar:<15} {len(node.jobs)}")
        
        print("="*60 + "\n")

def main():
    print("☸️  KUBERNETES-LIKE TASK SCHEDULER SIMULATOR\n")
    
    scheduler = Scheduler(algorithm="first-fit")
    
    # Submit jobs
    print("📋 Submitting Jobs...")
    scheduler.submit_job("job-1", cpu=2, memory=2, duration=2)
    scheduler.submit_job("job-2", cpu=1, memory=1, duration=1.5)
    scheduler.submit_job("job-3", cpu=3, memory=4, duration=2.5)
    scheduler.submit_job("job-4", cpu=2, memory=3, duration=1)
    scheduler.submit_job("job-5", cpu=1, memory=2, duration=2)
    
    print("\n🔄 Scheduling Jobs...")
    scheduler.schedule_jobs()
    
    time.sleep(1)
    scheduler.display_metrics()
    
    # Submit more jobs to trigger auto-scaling
    print("📋 Submitting More Jobs (Auto-scaling trigger)...")
    scheduler.submit_job("job-6", cpu=3, memory=3, duration=2)
    scheduler.submit_job("job-7", cpu=2, memory=2, duration=1.5)
    scheduler.submit_job("job-8", cpu=2, memory=3, duration=2)
    
    print("\n🔄 Scheduling Additional Jobs...")
    scheduler.schedule_jobs()
    
    time.sleep(1.5)
    
    # Simulate node failure
    print("\n⚠️  Simulating Node Failure...")
    scheduler.simulate_failure("node-2")
    scheduler.schedule_jobs()
    
    time.sleep(2)
    scheduler.display_metrics()
    
    # Wait for jobs to complete
    print("⏳ Waiting for jobs to complete...")
    time.sleep(3)
    
    scheduler.display_metrics()
    print("✅ Simulation Complete!")

if __name__ == "__main__":
    main()
