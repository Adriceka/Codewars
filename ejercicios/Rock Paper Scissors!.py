def rps(p1, p2):
    
    jugador1 = p1.capitalize()
    jugador2 = p2.capitalize()

    if jugador1 == jugador2:
        return "Draw!"

    gana_a = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock"}

    return "Player 1 won!" if gana_a[jugador1] == jugador2 else "Player 2 won!"

if __name__ == '__main__':
    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'paper') == "Player 1 won!"
    assert rps('paper', 'rock') == "Player 1 won!"
    assert rps('scissors', 'rock') == "Player 2 won!"
    assert rps('paper', 'scissors') == "Player 2 won!"
    assert rps('rock', 'paper') == "Player 2 won!"
    assert rps('rock', 'rock') == "Draw!"
    assert rps('scissors', 'scissors') == "Draw!"
    assert rps('paper', 'paper') == "Draw!"