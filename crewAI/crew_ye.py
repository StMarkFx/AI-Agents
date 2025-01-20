eifhieofhewiofhjefuigfeufguefuefvu
jrguidsuigdubshdbvsub
 def prompting_rag_task(self) -> Task:
        return Task(
            config=self.tasks_config['prompting_rag_task'],
            # tools=[rag_tool, query_instagram_db_tool],
            context=[self.merge_results_task()],
            # output_pydantic=ContentCreatorInfo,
            output_file="rag_output.md"