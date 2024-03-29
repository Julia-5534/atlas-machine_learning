#!/usr/bin/env python3
"""Task 32"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name"""
    result = mongo_collection.update_many(
        {"name": name}, {"$set": {"name": name, "topics": topics}})
    return result
