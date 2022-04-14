#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configurationParser
import pathlib
import tweepy
# Natural Language Processing
import spacy

PATH_TO_INIT_FILE = pathlib.Path.cwd().parent.joinpath('files', 'login_data.priv')
read_successful, cfg = configurationParser.get_configuration(PATH_TO_INIT_FILE, 'twitter')
auth = tweepy.OAuthHandler(cfg["consumer_key"], cfg["consumer_secret"])
auth.set_access_token(cfg["access_token"], cfg["access_token_secret"])
api = tweepy.API(auth)

nlp = spacy.load("de_core_news_sm")
text = ("GEHT WÄHLEN. #btw21"
        "Wählt so, dass ihr euch später nicht dafür schämen müsst, wenn eure (Enkel)Kinder aus dem Geschichts- "
        "und Geografieunterricht kommen & euch Fragen stellen."
        "Wählt weitsichtig. Wählt umsichtig. Wählt vielleicht mal anders als sonst. Aber vor allem: #noAfD"
        )


def main():
    try:
        api.verify_credentials()
        """last_tweet = api.home_timeline(count=1)[0]
        print(last_tweet.user.name)
        print(last_tweet.text)"""
        last_trends = api.get_place_trends(id="23424829")
        # print(type(last_trends[0]))
        # print(json.dumps(last_trends))
        # print(type(json.dumps(last_trends)))
        # print_json(json.dumps(last_trends))
        for element in last_trends[0]["trends"]:
            print(element["name"])

        """doc = nlp(text)
        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)"""

    except tweepy.TooManyRequests:
        print(tweepy.TooManyRequests.response)
    except tweepy.Unauthorized:
        print("Anmeldedaten nicht korrekt")


if __name__ == "__main__":
    main()
