from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .utils import update_productdata_table

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute="*/20")),
    name="task_update_productdata_table",
    ignore_result=True,
)
def task_update_productdata_table():
    """
    Updates the ProductData Table
    """
    update_productdata_table()
    logger.info("Upadated ProductData Table")