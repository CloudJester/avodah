import json
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.jobs import Job
from services.jobs import JobsService

router = APIRouter(
     prefix="/jobs",
)

job_service = JobsService()

@router.post("/")
async def post_job(job: Job):
    try:
        id = job_service.create_job(job)
        return {
            "response": "ok",
            "id": id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.delete("/{job_id}")
async def delete_job(job_id: str):
    try:
        id = job_service.delete_job(job_id)
        return {
            "response": "ok",
            "id": id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/")
async def get_jobs():
    try:
        jobs = job_service.get_jobs()
        json_compatible_item_data = jsonable_encoder(jobs)
        return {"response": json.dumps(json_compatible_item_data)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{job_id}")
async def get_job_by_id(job_id: str):
    try:
        jobs = job_service.get_job(job_id)
        return {"response": json.dumps(jobs.__dict__)}
    except Exception as e:
        # clean up by plumbing optional
        if "No Job Found" in str(e):
            raise HTTPException(status_code=404, detail="Job not found")