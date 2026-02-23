# Epic Title: Integrate with PostgreSQL for Data Storage

import logging
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()

def backup_job():
    from backend.admin_dashboard.controllers.backup_controller import create_backup
    create_backup()

def start_backup_scheduler():
    scheduler.add_job(backup_job, 'interval', hours=24)
    scheduler.start()
    logger.info("Backup scheduler started")

def stop_backup_scheduler():
    scheduler.shutdown()
    logger.info("Backup scheduler stopped")