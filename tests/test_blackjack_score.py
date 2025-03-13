from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

# # @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = ["King","Queen"]
  score = blackjack_score(hand)
  assert score == 20
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ["Ace","Jack"]
  score = blackjack_score(hand)
  assert score == 21
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = ["Ace","Ace",8]
  score = blackjack_score(hand)
  assert score == 20
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = ["banana","chicken","ace"]
  score = blackjack_score(hand)
  assert score == "Invalid"
#
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = ["king","Queen",5,8,6] #it should return
  score = blackjack_score(hand)
  assert score == "Invalid"
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = ["King","Ace",8]
  score = blackjack_score(hand)
  assert score == "bust"
#
# # @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = [ "King","Ace","Ace"]
  score = blackjack_score(hand)
  assert score == 12
#
# # @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  hand = ["Ace", "Ace", "Ace", "Ace"]
  score = blackjack_score(hand)
  assert score == 14