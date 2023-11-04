from project import answer_checker, final_score


def test_correct_answer_checker():
    user_answer = 1
    correct_answer = 1
    result = answer_checker(user_answer, correct_answer)
    expected_output = True
    assert result == expected_output


def test_wrong_answer_checker():
    user_answer = 2
    correct_answer = 4
    result = answer_checker(user_answer, correct_answer)
    expected_output = False
    assert result == expected_output


def test_final_score():
    score = 1
    question_amount = 2
    assert final_score(score, question_amount) == f"Your Score is: {score}/{question_amount}"

