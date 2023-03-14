from repositories.jobs import JobsRepository
from schemas.jobs import Job
from models.jobs import JobInternal

class JobsService:
    def __init__(self):
        self.repo = JobsRepository()

    def create_job(self, job: Job) -> int:
        return self.repo.create(_job_to_jobinternal(job))

    def get_jobs(self) -> list[Job]:
        jobinternals = self.repo.get()
        jobs = list[Job]()

        if not jobinternals:
            return jobs
        
        for jobinternal in jobinternals:
            jobs.append(_jobinternal_to_job(jobinternal))
        return jobs

    def get_job(self, id) -> Job:
        return _jobinternal_to_job(self.repo.get_by_id(id))
    
    def get_job_by_name(self, name) -> Job:
        return _jobinternal_to_job(self.repo.get_by_name(name))
 
    def delete_job(self, id):
        self.repo.delete(id)

def _job_to_jobinternal(job: Job) -> JobInternal:
    return JobInternal(job.id, job.name, job.image)


def _jobinternal_to_job(jobinternal: JobInternal) -> Job:
    return Job(
        id=jobinternal.id, 
        name=jobinternal.name, 
        image=jobinternal.image)