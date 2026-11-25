from sentiment import score, label


def test_positive():
    assert label(score("Excelente producto")) == "positivo"


def test_negative():
    assert label(score("Muy malo, se rompió")) == "negativo"


def test_negation_flips():
    assert score("no es malo") > 0


def test_neutral():
    assert label(score("Está bien")) == "neutro"


if __name__ == "__main__":
    test_positive()
    test_negative()
    test_negation_flips()
    test_neutral()
    print("ok")
