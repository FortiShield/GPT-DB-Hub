from typing import Optional, Dict, Any

from gptdb_hub.eval import evaluation


def start_evaluate(
    args: Optional[Dict[str, Any]] = None,
):
    # Arguments for evaluation
    if args is None:
        args = {
            "input": "./gptdb_hub/output/pred/pred_sql_dev_skeleton.sql",
            "gold": "./gptdb_hub/data/eval_data/gold.txt",
            "gold_natsql": "./gptdb_hub/data/eval_data/gold_natsql2sql.txt",
            "db": "./gptdb_hub/data/spider/database",
            "table": "./gptdb_hub/data/eval_data/tables.json",
            "table_natsql": "./gptdb_hub/data/eval_data/tables_for_natsql2sql.json",
            "etype": "exec",
            "plug_value": True,
            "keep_distict": False,
            "progress_bar_for_each_datapoint": False,
            "natsql": False,
        }
    else:
        args = args

    # Execute evaluation
    evaluation.evaluate_api(args)


if __name__ == "__main__":
    start_evaluate()
