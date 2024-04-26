import logging
import azure.functions as func
from main import main 

app = func.FunctionApp()

@app.schedule(
    schedule="0 0 */4 * * *", 
    arg_name="myTimer", 
    run_on_startup=True,
    use_monitor=True
) 
def olxrentschedule(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    main()
