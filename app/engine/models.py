# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Collection(models.Model):
    """
    Collection consists of multiple activities
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "{}".format(self.pk)


class KnowledgeComponent(models.Model):
    name = models.CharField(max_length=200)
    mastery_prior = models.FloatField()

    def __unicode__(self):
        return "{}".format(self.pk)


class PrerequisiteRelation(models.Model):
    prerequisite = models.ForeignKey(KnowledgeComponent, 
        related_name="dependent_relation"
    )
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()


class Activity(models.Model):
    """
    Activity model
    """
    name = models.CharField(max_length=200, default='')
    collection = models.ForeignKey(Collection)
    knowledge_components = models.ManyToManyField(KnowledgeComponent,blank=True)
    difficulty = models.FloatField(null=True,blank=True)
    tags = models.TextField(default='')
    type = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return "{}".format(self.pk)

# class Course(models.Model):
#     """
#     Course from which a learner can come from
#     """
#     name = models.CharField(max_length=200)


class Learner(models.Model):
    """
    User model for students
    """
    def __unicode__(self):
        return "{}".format(self.pk)


class Score(models.Model):
    """
    Score resulting from a learner's attempt on an activity
    """
    learner = models.ForeignKey(Learner)
    activity = models.ForeignKey(Activity)
    # score value
    score = models.FloatField()
    # creation time
    timestamp = models.DateTimeField(null=True,auto_now_add=True)


class Transit(models.Model):
    activity = models.ForeignKey(Activity)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()


class Guess(models.Model):
    activity = models.ForeignKey(Activity)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()

class Slip(models.Model):
    activity = models.ForeignKey(Activity)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()


class Mastery(models.Model):
    learner = models.ForeignKey(Learner)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()


class Exposure(models.Model):
    learner = models.ForeignKey(Learner)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.IntegerField()

class Confidence(models.Model):
    learner = models.ForeignKey(Learner)
    knowledge_component = models.ForeignKey(KnowledgeComponent)
    value = models.FloatField()


class EngineSettings(models.Model):
    name = models.CharField(max_length=200, default='')
    r_star = models.FloatField() #Threshold for forgiving lower odds of mastering pre-requisite LOs.
    L_star = models.FloatField() #Threshold logarithmic odds. If mastery logarithmic odds are >= than L_star, the LO is considered mastered
    W_p = models.FloatField() #Importance of readiness in recommending the next item
    W_r = models.FloatField() #Importance of demand in recommending the next item
    W_c = models.FloatField() #Importance of continuity in recommending the next item
    W_d = models.FloatField() #Importance of appropriate difficulty in recommending the next item

    def __unicode__(self):
        return "{}".format(self.pk)


