import numpy as np

def loss(y: int, h:int):
    """
    hinge loss for just two values

    Args
    y: true values
    h: predicted values

    Output
    hinge_loss: loss
    """
    hinge_loss = (0.1 - y*h)
    return hinge_loss


if __name__ == "__main__":
    print(loss(10, 2))
