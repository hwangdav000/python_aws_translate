import boto3


#translate from english to target language
#returns translated text
# en is english and es is spanish
def GetTranslation(text, target):
    client = boto3.client('translate', region_name='us-east-1')
    result = client.translate_text(Text=text, SourceLanguageCode ="en", TargetLanguageCode=target)
    return (result['TranslatedText'])