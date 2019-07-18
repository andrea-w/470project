import pandas

def calculate_accuracy():
    return

# returns the Mean Squared Error for a pandas Series of predicted test scores
# against the Series of the actual test scores
def calculate_MSE(actual_scores, predicted_scores):
    # first perform error checking
    if (actual_scores.len() != predicted_scores.len()):
        return "Error. Mismatch in length of arraylists of scores"
    N = actual_scores.len()
    squared_error = 0
    for i in range(N):
        squared_error += (actual_scores[i] - predicted_scores[i])**2
    # return average squared error
    return squared_error/N