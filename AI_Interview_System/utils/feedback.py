def generate_feedback(score):

    if score >= 80:

        return (
            "Excellent answer. "
            "Very relevant response."
        )

    elif score >= 60:

        return (
            "Good answer but "
            "needs more details."
        )

    elif score >= 40:

        return (
            "Average answer. "
            "Improve technical explanation."
        )

    else:

        return (
            "Poor answer. "
            "Need better understanding."
        )