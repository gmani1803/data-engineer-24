-- write your SQL here
SELECT
    EXTRACT(MONTH FROM TO_TIMESTAMP(t.datetime, 'YYYY-MM-DD HH24:MI:SS')) AS refund_month,
    EXTRACT(YEAR FROM TO_TIMESTAMP(t.datetime, 'YYYY-MM-DD HH24:MI:SS')) AS refund_year,
    oi.locationId,
    SUM(CAST(json_extract_path_text(t.details, 'items', '0', 'amount') AS NUMERIC)) AS total_refund_amount
FROM
    transaction_data t
JOIN
    order_items oi ON CAST(json_extract_path_text(t.details, 'items', '0', 'id') AS INTEGER) = oi.id
WHERE
    t.type = 'refund'
GROUP BY
    refund_month,
    refund_year,
    oi.locationId
ORDER BY
    refund_year,
    refund_month,
    oi.locationId;
