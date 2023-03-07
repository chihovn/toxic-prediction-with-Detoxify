from detoxify import Detoxify
import logging
import pandas as pd
from pathlib import Path
from src.timeit import *
from src.argument import *
from src.utils import *

logger = logging.getLogger(__name__)

@timeit
def load_model(model_name):
    # logger.info("Start loading model")
    model = Detoxify(model_name)
    # logger.info("End loading model")
    return model

@timeit
def load_data(input_path):
    df = pd.read_csv(input_path)
    return df['text'].tolist()

@timeit
def main():
    # init logger
    init_loger('.log/log.txt')
    logger.info('========================================== START A NEW TURN ==========================================')
    
    # load argument
    args = Arguments()
    args = args.parse() # get argument object

    # normalize input arguments
    logger.info('Normalizing input arguments...')
    args.model_name = args.model_name.lower()
    args.mode = args.mode.lower()

    if args.model_name != 'original' and args.model_name != 'unbiased':
        logger.info('Only work with "original" or "unbiased" model. Please try again!')
    else: 
        logger.info('Loading Detoxify "{}" model...'.format(args.model_name))
        model = load_model(args.model_name)

        if args.mode == 'qa':
            logger.info("============== QA MODE ==============")
            while True:
                input_text = input('Enter your text: ')
                logger.info("Input text: {}".format(input_text))
                score = model.predict(input_text)['toxicity']
                logger.info('Toxicity score: {}'.format(score))
                is_continued = input("Continue? (Y/N): ")
                if is_continued.lower() == 'y' or is_continued == 'yes':
                    pass
                else:
                    break
        elif args.mode == 'csv':
            try:
                logger.info("Loading data from {}...".format(args.input_path))
                data = load_data(args.input_path)
            except FileNotFoundError:
                logger.info("No such file or directory. Try to enter another input_path")
            except:
                logger.info("Something else went wrong when loading data")
            else:
                scores = []
                for text in data:
                    scores.append(model.predict(text)['toxicity'])
                df = pd.DataFrame(list(zip(data, scores)), columns =['text', 'toxicity score'])
                save_to_csv(args.save_to, df)
                logger.info('Saved result to {}'.format(args.save_to))           
        else:
            logger.info('Only work with "qa" or "csv" mode. Please try again!')


if __name__ == "__main__":
    main()