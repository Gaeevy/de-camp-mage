-- 1
SELECT count(*) FROM de-camp-42.gt_2022.external_yellow_tripdata limit 10;

-- 2
select
  count(distinct pu_location_id)
from de-camp-42.gt_2022.external_yellow_tripdata
limit 100;

select
  count(distinct pu_location_id)
from de-camp-42.gt_2022.yellow_tripdata_non_partitoned
limit 100;

-- 3
select
  count(*)
from de-camp-42.gt_2022.yellow_tripdata_non_partitoned
where fare_amount = 0;

-- 4
CREATE OR REPLACE TABLE de-camp-42.gt_2022.yellow_tripdata_partitoned_clustered
PARTITION BY lpep_pickup_date
CLUSTER BY pu_location_id AS
SELECT * FROM de-camp-42.gt_2022.external_yellow_tripdata;

-- 5
select
  distinct pu_location_id
from de-camp-42.gt_2022.yellow_tripdata_non_partitoned
where lpep_pickup_date BETWEEN '2022-06-01' and '2022-06-30';

select
  distinct pu_location_id
from de-camp-42.gt_2022.yellow_tripdata_partitoned_clustered
where lpep_pickup_date BETWEEN '2022-06-01' and '2022-06-30'
