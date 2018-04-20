from celeryrun import app
import subprocess

@app.task
def run_10min():
    runner = subprocess.Popen('python3 /home/linhanqiu/crawler240/KTspider/run.py',shell=True)
    runner.wait()
    return "end"