## Project Requirements Document for AI Detector

### Unit Tests

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application must correctly resolve the URL for the index view. | When the reverse('index') function is called. | The resolved URL should map to the index view function. | test_index_url_is_resolved
The application must correctly resolve the URL for the AI detector view. | When the reverse('ai_detector') function is called. | The resolved URL should map to the ai_detector view function. | test_ai_detector_url_is_resolved
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200, use the index.html template. The response must contain the text 'AI Detector Home'. | test_index_get
The AI detector view must handle GET requests correctly. | When a GET request is made to the AI detector URL. | The response should have a status code of 200 and use the result.html template. The response must contain the text 'AI Detector Result'. | test_ai_detector_get
The AI detector view must handle POST requests correctly. | When a POST request with valid data is made to the AI detector URL. | The response should have a status code of 200. The response must contain the text 'AI Detector Result' and include the message 'Back to AI Detector>>>.'. | test_ai_detector_post
The application must handle non-existent URLs correctly. | When a GET request is made to a non-existent URL. | The response should have a status code of 404 and use the 404.html template. The response must contain the text 'AI Detector Page not found'. | test_handler404
The get_score function must handle cases where the input data is empty or invalid. | When the input data is an empty dictionary ({}). | The function should return the string "Error". | test_get_score_error
The get_score function must compare the scores of labels within the provided data. | When LABEL_0 has a higher score than LABEL_1 in the input data. | The function should return False. | test_get_score_label0_gt_label1
The get_score function must compare the scores of labels within the provided data. | When LABEL_0 has a lower score than LABEL_1 in the input data. | The function should return True. | test_get_score_label0_lt_label1

