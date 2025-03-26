with base as (
    select * from {{ ref('stg_cc_cedict') }}
),

split_defs as (
    select
        *,
        string_split(definitions, '/') as def_array
    from base
),

filtered as (
    select
        simplified,
        traditional,
        pinyin,
        array_filter(def_array, d -> not d ilike 'Taiwan pr.%') as english_definitions
    from split_defs
)

select * from filtered