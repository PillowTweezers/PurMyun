import math

from src.Weights import Weights


class Participant:
    def __init__(self, data: dict):
        self.name = data.get("שם מלא:")
        self.grade = data.get("שכבה:")
        self.team_preference1 = data.get("דרגו את הצוותים שאתם רוצים להיות בהם: [עדיפות ראשונה]")
        self.team_preference2 = data.get("דרגו את הצוותים שאתם רוצים להיות בהם: [עדיפות שניה]")
        self.team_preference3 = data.get("דרגו את הצוותים שאתם רוצים להיות בהם: [עדיפות שלישית]")
        self.motivation = int(data.get("מהי רמת המוטיבציה שלכם להליך פורימון?"))
        self.presence = int(data.get("לכמה ימי עבודה אתם מתכוונים להגיע?"))
        self.square = int(data.get("מהי רמת הכפיתה המרובעת שלך?"))
        self.cross = int(data.get("מהי רמת הכפיתה המוצלבת שלך?"))
        self.parallel = int(data.get("מהי רמת הכפיתה המקבילה שלך?"))
        self.tripod = int(data.get("מהי רמת כפיתת החצובה שלך?"))
        self.anchoring = int(data.get("מהי רמת עיגון היתרים שלך?"))
        self.macrame = int(data.get("מהי רמת המקרמה שלך?"))
        self.appearance = int(data.get("כמה אתם מעוניינים להיות בצוות חזות?"))

    def calculateProfession(self, weights: Weights):
        score = 0
        score += self.square * weights.square / 5
        score += self.cross * weights.cross / 5
        score += self.parallel * weights.parallel / 5
        score += self.tripod * weights.tripod / 5
        score += self.anchoring * weights.anchoring / 5
        score += self.macrame * weights.macrame / 5
        return score

    def calculateMotivation(self):
        # iteration 1:
        # return (math.sqrt(self.motivation) * math.pow(self.presence, 2)) / self.appearance
        # iteration 2:
        # return (self.presence / 2) ** 2 * math.sqrt(self.motivation + 4)
        # iteration 3:
        return (math.pow(math.log10(self.presence), 3) + (self.motivation - 1) / 40) / 1.1

    def calculateGrade(self, weights: Weights):
        return self.calculateProfession(weights) * self.calculateMotivation()

    def __str__(self):
        return f"{self.name} - {self.grade} - {self.team_preference1} - {self.team_preference2} - {self.team_preference3} - {self.motivation} - {self.square} - {self.cross} - {self.parallel} - {self.tripod} - {self.anchoring} - {self.macrame} - {self.appearance}"
