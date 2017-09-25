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
    
    def devtest(self):
        for name, tag in self.devtest_names:
            guess = self.classifier.classify(self.gender_features(name))
            if guess != tag:
                print 'tag=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

    def build(self):
        names = self.load()

        train_names, devtest_names, test_names = names[1500:], names[500:1500], names[:500]
        train_set = apply_features(self.gender_features, train_names)
        devtest_set = apply_features(self.gender_features, devtest_names)
        test_set = apply_features(self.gender_features, test_names)
    
        classifier = nltk.NaiveBayesClassifier.train(train_set)
    
        accuracy = nltk.classify.accuracy(classifier, devtest_set)
        print ("devtest Accuracy: ", accuracy)
        accuracy = nltk.classify.accuracy(classifier, test_set)
        print ("test Accuracy: ", accuracy)

        print classifier.show_most_informative_features(5)
    
        self.classifier = classifier
        self.devtest_names = devtest_names

        self.devtest()

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
