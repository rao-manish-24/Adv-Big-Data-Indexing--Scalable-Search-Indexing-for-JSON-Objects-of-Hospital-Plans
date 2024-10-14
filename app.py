import threading
from src import config, app
from src.consumer import RabbitMQConsumer

consumer = RabbitMQConsumer()

def start_consumer():
    consumer.start()

if __name__ == "__main__":
    app.logger.info("Server started running at {}:{}".format(config.HOST, config.PORT))
    
    # Start the consumer in a separate thread
    consumer_thread = threading.Thread(target=start_consumer)
    consumer_thread.start()
    
    with app.app_context():
        try:
            app.run(
                host=config.HOST,
                port=config.PORT,
                debug=config.DEBUG,
                # ssl_context="adhoc"
            )
        finally:
            app.logger.info("Server terminated at {}:{}".format(config.HOST, config.PORT))
            consumer.stop()
            consumer_thread.join()
