#!/usr/bin/env python
# -*- coding: utf-8 -*-
# module:
# author:

import csv
import json
import os


def write_header(file_name, columns):
    with open(file_name,'w', encoding="utf-8") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(columns)

if not os.path.isfile("data/business_header.csv"):
    with open("dataset/business.json",encoding="utf-8") as business_json, \
            open("data/business.csv", 'w',encoding="utf-8") as business_csv:

        write_header("data/business_header.csv", ['id:ID(Business)', 'name', 'address', 'city', 'state'])

        business_writer = csv.writer(business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in business_json.readlines():
            item = json.loads(line)
            try:
                business_writer.writerow([item['business_id'], item['name'], item['address'], item['city'], item['state']])
            except Exception as e:
                print(item)
                raise e

if not os.path.isfile("data/city_header.csv"):
    with open("dataset/business.json", encoding="utf-8") as business_json, \
            open("data/city.csv", "w", encoding="utf-8") as city_csv, \
            open("data/business_IN_CITY_city.csv", "w", encoding="utf-8") as business_city_csv:

        write_header("data/city_header.csv", ['name:ID(City)'])
        write_header("data/business_IN_CITY_city_header.csv", [':START_ID(Business)', ':END_ID(City)'])

        business_city_writer = csv.writer(business_city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        city_writer = csv.writer(city_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_cities = set()
        for line in business_json.readlines():
            item = json.loads(line)

            if item["city"].strip():
                unique_cities.add(item["city"])
                business_city_writer.writerow([item["business_id"], item["city"]])

        for city in unique_cities:
            city_writer.writerow([city])

if not os.path.isfile("data/area_header.csv"):
    with open("dataset/businessLocations.json", encoding="utf-8") as business_locations_json, \
            open("data/area.csv", "w",encoding="utf-8") as area_csv, \
            open("data/country.csv", "w",encoding="utf-8") as country_csv, \
            open("data/city_IN_AREA_area.csv", "w",encoding="utf-8") as city_area_csv, \
            open("data/area_IN_COUNTRY_country.csv", "w",encoding="utf-8") as area_country_csv:
        input = json.load(business_locations_json)

        write_header("data/area_header.csv", ['name:ID(Area)'])
        write_header("data/country_header.csv", ['name:ID(Country)'])

        write_header("data/city_IN_AREA_area_header.csv", [':START_ID(City)', ':END_ID(Area)'])
        write_header("data/area_IN_COUNTRY_country_header.csv", [':START_ID(Area)', ':END_ID(Country)'])

        area_writer = csv.writer(area_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        country_writer = csv.writer(country_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        city_area_writer = csv.writer(city_area_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        area_country_writer = csv.writer(area_country_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        unique_areas = set()
        unique_countries = set()
        unique_city_areas = set()
        unique_area_countries = set()

        for business_id in input:
            if input[business_id]["admin1"]:
                unique_areas.add(input[business_id]["admin1"])
                unique_countries.add(input[business_id]["country"])

                unique_city_areas.add((input[business_id]["city"], input[business_id]["admin1"]))
                unique_area_countries.add((input[business_id]["admin1"], input[business_id]["country"]))

        for area in unique_areas:
            area_writer.writerow([area])

        for country in unique_countries:
            country_writer.writerow([country])

        for city, area in unique_city_areas:
            city_area_writer.writerow([city, area])

        for area, country in unique_area_countries:
            area_country_writer.writerow([area, country])

if not os.path.isfile("data/category_header.csv"):
    with open("dataset/business.json", encoding="utf-8") as business_json, \
            open("data/category.csv", 'w', encoding="utf-8") as categories_csv, \
            open("data/business_IN_CATEGORY_category.csv", 'w', encoding="utf-8") as business_category_csv:

        write_header("data/category_header.csv", ['name:ID(Category)'])
        write_header("data/business_IN_CATEGORY_category_header.csv", [':START_ID(Business)', ':END_ID(Category)'])

        business_category_writer = csv.writer(business_category_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        category_writer = csv.writer(categories_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
                
        unique_categories = set()
        for line in business_json.readlines():
            item = json.loads(line)
            
            if item["categories"] is not None:
                for category in item["categories"].split(','):
                    unique_categories.add(category.strip())
                    business_category_writer.writerow([item["business_id"], category])
                
        for category in unique_categories:
            try:
                category_writer.writerow([category])
            except Exception as e:
                print(category)
                raise e     
                        

if not os.path.isfile("data/user_header.csv"):
    with open("dataset/user.json", encoding="utf-8") as user_json, \
            open("data/user.csv", 'w', encoding="utf-8") as user_csv, \
            open("data/user_FRIENDS_user.csv", 'w', encoding="utf-8") as user_user_csv:

        write_header("data/user_header.csv", ['id:ID(User)', 'name'])
        write_header("data/user_FRIENDS_user_header.csv", [':START_ID(User)', ':END_ID(User)'])

        user_writer = csv.writer(user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_user_writer = csv.writer(user_user_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in user_json.readlines():
            item = json.loads(line)
            user_writer.writerow([item["user_id"], item["name"]])

            if item["friends"] is not None:
                for friend_id in item["friends"].split(','):
                    user_user_writer.writerow([item["user_id"], friend_id.strip()])

                
                
if not os.path.isfile("data/review_header.csv"):
    with open("dataset/review.json", encoding="utf-8") as review_json, \
            open("data/review.csv", 'w', encoding="utf-8") as review_csv, \
            open("data/user_WROTE_review.csv", 'w', encoding="utf-8") as user_review_csv, \
            open("data/review_REVIEWS_business.csv", 'w', encoding="utf-8") as review_business_csv:

        write_header("data/review_header.csv", ['id:ID(Review)', 'text', 'stars', 'date'])
        write_header("data/user_WROTE_review_header.csv", [':START_ID(User)', ':END_ID(Review)'])
        write_header("data/review_REVIEWS_business_header.csv", [':START_ID(Review)', ':END_ID(Business)'])

        review_writer = csv.writer(review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        user_review_writer = csv.writer(user_review_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)
        review_business_writer = csv.writer(review_business_csv, escapechar='\\', quotechar='"', quoting=csv.QUOTE_ALL)

        for line in review_json.readlines():
            item = json.loads(line)
            review_writer.writerow([item["review_id"], item["text"], item["stars"], item["date"]])
            user_review_writer.writerow([item["user_id"], item["review_id"]])
            review_business_writer.writerow([item["review_id"], item["business_id"]])