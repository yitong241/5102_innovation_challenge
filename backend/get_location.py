from transformers import DistilBertTokenizer, DistilBertForTokenClassification, AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load pre-trained model and tokenizer
def get_location_LLM(text):
    print(text)
    # model_name = "elastic/distilbert-base-cased-finetuned-conll03-english"
    # model_name = "dbmdz/bert-base-turkish-cased"
    model_name = "dslim/bert-base-NER"
    # tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    # model = DistilBertForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Create a NER pipeline
    ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

    # Example text
    # text = "what is the current flow in Tuas Checkpoint?"

    # Use the pipeline to predict entities
    entities = ner_pipeline(text)
    print(entities)

    # Extract and print locations
    locations = [entity['word'] for entity in entities if entity['entity'] == 'I-LOC' or entity['entity'] == 'B-LOC']

    res = []
    print("--------------------")
    print(locations)
    temp = locations[0]
    for i in range(1, len(locations)):
        if locations[i][0] == "#":
            temp = temp + locations[i][2:]
        else:
            res.append(temp)
            temp = locations[i]
    res.append(temp)
    search_location = ' '.join(res)
    print('The location the user wishes to inquire about is {}'.format(search_location))
    return search_location

