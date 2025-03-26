# CC-Cedict-dbt


Install requirements:

```
pip install dbt-duckdb
pip install -U recce

```


Download the latest version of the cc-cedict dictionary:

```
python scripts/cc_cedict_download.py
```

Create the dbt seeds CSV:

```
python scripts/cc_cedict_seeds.py
```

Seed:
```
dbt seed
```

Run dbt
```
dbt run
```

Generate docs:
```
dbt docs generate
```

Run Recce:
```
recce server
```



Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
