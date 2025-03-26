with source as (
    select * from {{ ref('cc_cedict') }}
),

cleaned as (
    select
        lower(simplified) as simplified,
        lower(traditional) as traditional,
        pinyin,
        definitions
    from source
    where simplified is not null
)

select * from cleaned