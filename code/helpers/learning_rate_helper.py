def alpha_for_epoch(epoch, epochs_total, alpha_max, alpha_min, learning_rate_type):
    if epochs_total == 1:
        return alpha_max

    if learning_rate_type == 'linear':
        alpha_delta = (alpha_max - alpha_min) / (epochs_total - 1)
        return alpha_max - alpha_delta * (epoch - 1)

    if learning_rate_type == 'exp':
        step = (alpha_min / alpha_max) ** (1. / (epochs_total - 1))
        return alpha_max * step ** (epoch - 1)
