

    DEFAULT_REFINE_PROMPT_TMPL = (
        "HUMAN : The original question is as follows: {query_str}\n"
        "We have provided an existing answer: {existing_answer}\n"
        "We have the opportunity to refine the existing answer "
        "(only if needed) with some more context below.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Given the new context, refine the original answer to better "
        "answer the question. "
        "If the context isn't useful, return the original answer.\n"
        "ASSISTANT:"
    )

    DEFAULT_REFINE_PROMPT = Prompt(
        DEFAULT_REFINE_PROMPT_TMPL, prompt_type=PromptType.REFINE
    )


    template1 = (
        "HUMAN : We have provided context information below. \n"
        "---------------------\n"
        "{context_str}"
        "\n---------------------\n"
        "Given this information, please answer the question: {query_str}\n"
        "ASSISTANT:"
    )