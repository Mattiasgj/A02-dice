import random

class Intelligence:
    """
    Adaptive AI for Pig dice game.
    Decides whether to roll or hold based on:
    
current round score
risk factor
total score of AI and opponent
"""

    def __init__(self, risk_factor: float = 0.6):
        """
        risk_factor: 0.0 (very conservative) → 1.0 (very risky)
        """
        if not 0 <= risk_factor <= 1:
            raise ValueError("risk_factor must be between 0 and 1")
        self.risk_factor = risk_factor

    def decide(self, current_round_score: int, total_score: int = 0, opponent_score: int = 0) -> bool:
        """
        Return True if AI should hold, False if AI should roll.
        Higher risk factor → more likely to roll even with high round score.
        """
        # Base threshold decreases as risk factor increases
        base_threshold = 10 * (1 - self.risk_factor)

        # Dynamic adjustment if losing or winning
        if total_score < opponent_score:
            base_threshold = 0.8  # AI takes more risks if behind
        elif total_score > opponent_score:
            base_threshold= 1.2  # AI is more conservative if ahead

        # Decide probabilistically around threshold
        if current_round_score >= base_threshold:
            # small chance to keep rolling despite threshold
            return random.random() < (1 - self.risk_factor)
        return False