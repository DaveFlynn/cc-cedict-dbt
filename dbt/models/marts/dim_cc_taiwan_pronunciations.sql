with base as (
    select * from {{ ref('stg_cc_cedict') }}
),

split_defs as (
    select
        *,
        string_split(definitions, '/') as def_array
    from base
),

taiwan as (
    select
        simplified,
        traditional,
        regexp_extract(definition, '\\[(.*?)\\]') as taiwan_pinyin
    from split_defs,
    unnest(def_array) as d(definition)
    where definition ilike 'Taiwan pr.%'
)

select * from taiwan