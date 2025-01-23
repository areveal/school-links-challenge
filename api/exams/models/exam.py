from django.db import models


class Exam(models.Model):
    """Represents a single type of Exam"""
    class StateChoices(models.TextChoices):
        ALABAMA = 'AL', 'Alabama'
        ALASKA = 'AK', 'Alaska'
        ARIZONA = 'AZ', 'Arizona'
        ARKANSAS = 'AR', 'Arkansas'
        CALIFORNIA = 'CA', 'California'
        COLORADO = 'CO', 'Colorado'
        CONNECTICUT = 'CT', 'Connecticut'
        DELAWARE = 'DE', 'Delaware'
        FLORIDA = 'FL', 'Florida'
        GEORGIA = 'GA', 'Georgia'
        HAWAII = 'HI', 'Hawaii'
        IDAHO = 'ID', 'Idaho'
        ILLINOIS = 'IL', 'Illinois'
        INDIANA = 'IN', 'Indiana'
        IOWA = 'IA', 'Iowa'
        KANSAS = 'KS', 'Kansas'
        KENTUCKY = 'KY', 'Kentucky'
        LOUISIANA = 'LA', 'Louisiana'
        MAINE = 'ME', 'Maine'
        MARYLAND = 'MD', 'Maryland'
        MASSACHUSETTS = 'MA', 'Massachusetts'
        MICHIGAN = 'MI', 'Michigan'
        MINNESOTA = 'MN', 'Minnesota'
        MISSISSIPPI = 'MS', 'Mississippi'
        MISSOURI = 'MO', 'Missouri'
        MONTANA = 'MT', 'Montana'
        NEBRASKA = 'NE', 'Nebraska'
        NEVADA = 'NV', 'Nevada'
        NEW_HAMPSHIRE = 'NH', 'New Hampshire'
        NEW_JERSEY = 'NJ', 'New Jersey'
        NEW_MEXICO = 'NM', 'New Mexico'
        NEW_YORK = 'NY', 'New York'
        NORTH_CAROLINA = 'NC', 'North Carolina'
        NORTH_DAKOTA = 'ND', 'North Dakota'
        OHIO = 'OH', 'Ohio'
        OKLAHOMA = 'OK', 'Oklahoma'
        OREGON = 'OR', 'Oregon'
        PENNSYLVANIA = 'PA', 'Pennsylvania'
        RHODE_ISLAND = 'RI', 'Rhode Island'
        SOUTH_CAROLINA = 'SC', 'South Carolina'
        SOUTH_DAKOTA = 'SD', 'South Dakota'
        TENNESSEE = 'TN', 'Tennessee'
        TEXAS = 'TX', 'Texas'
        UTAH = 'UT', 'Utah'
        VERMONT = 'VT', 'Vermont'
        VIRGINIA = 'VA', 'Virginia'
        WASHINGTON = 'WA', 'Washington'
        WEST_VIRGINIA = 'WV', 'West Virginia'
        WISCONSIN = 'WI', 'Wisconsin'
        WYOMING = 'WY', 'Wyoming'

    class GradeLevelChoices(models.TextChoices):
        PRE_K = 'PK', 'Pre-Kindergarten'
        KINDERGARTEN = 'K', 'Kindergarten'
        FIRST = '1', '1st Grade'
        SECOND = '2', '2nd Grade'
        THIRD = '3', '3rd Grade'
        FOURTH = '4', '4th Grade'
        FIFTH = '5', '5th Grade'
        SIXTH = '6', '6th Grade'
        SEVENTH = '7', '7th Grade'
        EIGHTH = '8', '8th Grade'
        NINTH = '9', '9th Grade (Freshman)'
        TENTH = '10', '10th Grade (Sophomore)'
        ELEVENTH = '11', '11th Grade (Junior)'
        TWELFTH = '12', '12th Grade (Senior)'
        COLLEGE_FRESHMAN = 'C1', 'College Freshman'
        COLLEGE_SOPHOMORE = 'C2', 'College Sophomore'
        COLLEGE_JUNIOR = 'C3', 'College Junior'
        COLLEGE_SENIOR = 'C4', 'College Senior'

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    max_score = models.IntegerField(null=True)
    state = models.TextField(choices=StateChoices.choices, max_length=30, null=True, default=None)
    subject = models.CharField(max_length=100, null=True, default=None)
    grade = models.TextField(choices=GradeLevelChoices.choices, max_length=20, null=True, default=None)
    properties = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.name} ({self.code})"
