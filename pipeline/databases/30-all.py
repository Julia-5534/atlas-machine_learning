#!/usr/bin/env python3
"""Task 30"""

def list_all(mongo_collection):
    """Function to list all documents in a collection"""
    documents = mongo_collection.find()
    return documents
