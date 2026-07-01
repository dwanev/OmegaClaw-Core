import lib_llm_ext


def perform_query(user_prompt = "remember that the morning standup is at 10am"):
    with open("./memory/prompt.txt") as f:
        system_prompt = " ".join(f.readlines())

        # 1. Explicitly register the OllamaProvider instance to overwrite
        # the default placeholder registration in your script.
        ollama_prov = lib_llm_ext.OllamaProvider(
            name="Ollama-local",
            var_name="OLLAMA_API_KEY",
            model_name="gemma4:e4b",
            base_url="http://localhost:11434/api/chat"
        )
        lib_llm_ext._register_provider_instance(ollama_prov)

        # 2. Define the user query
    #     prompt = """
    # Task: Propose an architecture for a local-first AI writing app.
    # Constraints: Prioritize privacy, low latency, and offline fallback.
    # Output format:
    # 1. Recommended architecture
    # 2. Key tradeoffs
    # 3. Failure modes
    # 4. Final recommendation"""

        full_prompt = system_prompt + ":-:-:-:" + user_prompt

        try:
            # 3. Execute via your existing callProvider dispatcher
            output = lib_llm_ext.callProvider(
                provider_name="Ollama-local",
                content=full_prompt,
                max_tokens=2000
            )
            # print("=" * 60)
            # print("FINAL OUTPUT:")
            # print(output if output.strip() else "[No content returned or exception occurred]")
            return output
        except RuntimeError as e:
            print(f"\nConfiguration Error: {e}")
        except Exception as e:
            print(f"\nUnexpected Error during execution: {e}")


def perform_query_1():
    user_prompt = "remember that the morning standup is at 10am"
    answer = perform_query(user_prompt)
    print("Sent:    ", user_prompt)
    print("=== LLM Response Start ===\n", answer, "\n=== LLM Response End ===")

def perform_query_2():
    user_prompt = "remember that the morning standup is at 10am and then search for good resturants near washington state university"
    answer = perform_query(user_prompt)
    print("Sent:    ", user_prompt)
    print("=== LLM Response Start ===\n", answer, "\n=== LLM Response End ===")

def load_and_test_example_file():
    with open("./prompt_reply_test_cases.txt") as f:
        full_file = "\n".join(f.readlines())
        full_file = full_file.replace("\n\n", "\n")
        test_cases = full_file.split("\nuser_request\n")
        for i, test_case in enumerate(test_cases):
            if i > 0: # skip the info in first position.
                fields = test_case.split("\nexpected_response\n")
                if len(fields) == 2:
                    user_request = fields[0]
                    expected_response = fields[1]
                    answer = perform_query(user_request)
                    print("user_request:", user_request.strip())
                    print("Got:         ", answer.strip())
                    print("Expected:    ", expected_response.strip())
                    # assert answer.strip() == expected_response.strip()

if __name__ == "__main__":
    # perform_query_1()
    # perform_query_2()
    load_and_test_example_file()