#!/usr/bin/env python
# coding=utf-8

import nltk
from nltk.corpus import names
from nltk.classify import apply_features
import random

class Gender:
    def gender_features(self, word):
        return {'last_letter': word[-1]}
    
    def load(self):
        get_names = ([(name, 'male') for name in names.words('male.txt')] + \
                [(name, 'female') for name in names.words('female.txt')])
    
        random.shuffle(get_names)
    
        return get_names
    
    def build(self):
        names = self.load()

        train_set = apply_features(self.gender_features, names[500:])
        test_set = apply_features(self.gender_features, names[:500])
    
        classifier = nltk.NaiveBayesClassifier.train(train_set)
    
        accuracy = nltk.classify.accuracy(classifier, test_set)
        print ("Accuracy: ", accuracy)
    
        print classifier.show_most_informative_features(5)
    
        self.classifier = classifier

        return self.classifier
    
    def forecast(self, name):
        return self.classifier.classify(self.gender_features(name))

if __name__ == '__main__':
    fit = Gender()
    
    fit.build()

    gender = fit.forecast('Neo')
    print 'Neo maybe ' + gender

    gender = fit.forecast('Trinity')
    print 'Trinity maybe ' + gender

    gender = fit.forecast('Alphagao')
    print 'Alphagao maybe ' + gender
