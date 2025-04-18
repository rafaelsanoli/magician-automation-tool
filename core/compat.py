from core.scheduler import Scheduler

def load_schedule_config(config_path="config/workflows.json"):
    return Scheduler(config_path).load_config()