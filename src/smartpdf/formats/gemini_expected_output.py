GenerateContentResponse(
    done=True,
    iterator=None,
    result=glm.GenerateContentResponse({
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "Yes, I am live \n"
              }
            ],
            "role": "model"
          },
          "finish_reason": 1,
          "index": 0,
          "safety_ratings": [
            {
              "category": 9,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 8,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 7,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 10,
              "probability": 1,
              "blocked": false
            }
          ],
          "token_count": 0,
          "grounding_attributions": []
        }
      ],
      "usage_metadata": {
        "prompt_token_count": 16,
        "candidates_token_count": 5,
        "total_token_count": 21
      }
    }),
)