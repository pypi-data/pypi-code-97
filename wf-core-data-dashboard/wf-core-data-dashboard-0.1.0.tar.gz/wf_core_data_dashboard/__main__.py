import uvicorn

from wf_core_data_dashboard.app import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
