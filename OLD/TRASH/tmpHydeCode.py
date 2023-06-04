            print("HYDE vanilla generation :")
            with open(PROMPTFILEHYDE, 'r') as file:
                prt = file.read()
            PRT = PromptTemplate(template=prt, input_variables=["question"])
            hydeChain = LLMChain(llm=llamamodel, prompt=PRT)
            hydeEmbeddings = HypotheticalDocumentEmbedder(llm_chain=hydeChain, base_embeddings=embeddings_function())     
            result = hydeEmbeddings.embed_query(query)

            context =  db.max_marginal_relevance_search_by_vector(result, k=4, lambda_mult=0.9)
            print(f"Context for {query} : ")
            inputcontext=build_string_context(context)         
            inputsdict = {"context": inputcontext, "question": query}