import google.generativeai as genai
from fastapi import APIRouter, HTTPException
import requests
from typing import Dict, List, Optional
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
import aiohttp
import asyncio

router = APIRouter()

# Initialize Google AI
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))
model = genai.GenerativeModel('gemini-pro')

class AIService:
    @staticmethod
    async def generate_content(prompt: str, content_type: str) -> str:
        try:
            # Customize system message based on content type
            context_prompts = {
                'blog': "You are an expert affiliate marketing content writer. Create engaging blog content that naturally incorporates affiliate products. Format the response in markdown.",
                'social': "You are a social media expert. Create engaging, platform-appropriate content for affiliate marketing. Include hashtag suggestions.",
                'email': "You are an email marketing specialist. Create compelling email content that drives affiliate conversions. Include subject line suggestions.",
                'review': "You are a product reviewer. Create honest, detailed reviews that highlight product benefits and include affiliate context. Format in markdown."
            }

            full_prompt = f"{context_prompts.get(content_type, context_prompts['blog'])}\n\nTask: {prompt}"
            response = await model.generate_content_async(full_prompt)
            return response.text

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def optimize_link(url: str, optimization_type: str) -> Dict:
        try:
            if optimization_type == 'analyze':
                # Use Google AI for link analysis
                analysis_prompt = f"""
                Analyze this URL for affiliate marketing optimization: {url}
                Provide insights on:
                1. URL structure and readability
                2. Trust factors
                3. Conversion optimization suggestions
                4. Mobile optimization
                Format the response as a JSON object with these keys: title, analysis_points, recommendations
                """
                response = await model.generate_content_async(analysis_prompt)
                return json.loads(response.text)

            elif optimization_type == 'shorten':
                # Use built-in URL shortener
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'http://tinyurl.com/api-create.php?url={url}') as response:
                        shortened_url = await response.text()
                        return {'shortened_url': shortened_url}

            elif optimization_type == 'tracking':
                # Add UTM parameters
                utm_params = {
                    'utm_source': 'affiliate',
                    'utm_medium': 'link',
                    'utm_campaign': datetime.now().strftime('%Y%m')
                }
                separator = '&' if '?' in url else '?'
                tracking_url = f"{url}{separator}" + '&'.join([f"{k}={v}" for k, v in utm_params.items()])
                return {'tracking_url': tracking_url}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def analyze_audience(niche: str, analysis_type: str) -> Dict:
        try:
            prompts = {
                'demographics': f"""
                Analyze the demographic characteristics of the target audience for the {niche} niche in affiliate marketing.
                Include:
                1. Age groups
                2. Income levels
                3. Education
                4. Geographic distribution
                5. Buying habits
                Format as JSON with keys: demographics, characteristics, opportunities
                """,
                'interests': f"""
                Map the interests and preferences of people interested in {niche}.
                Include:
                1. Primary interests
                2. Related niches
                3. Content preferences
                4. Platform usage
                5. Brand affinities
                Format as JSON with keys: interests, related_niches, platforms, recommendations
                """,
                'behavior': f"""
                Analyze the online behavior patterns of {niche} audience.
                Include:
                1. Purchase behavior
                2. Decision factors
                3. Research habits
                4. Platform preferences
                5. Content consumption
                Format as JSON with keys: behaviors, patterns, triggers, optimization_tips
                """
            }

            response = await model.generate_content_async(prompts[analysis_type])
            return json.loads(response.text)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def analyze_trends(market: str, trend_type: str) -> Dict:
        try:
            prompts = {
                'market': f"""
                Analyze current market trends in {market}.
                Include:
                1. Growing trends with growth percentages
                2. Market sentiment
                3. Related product categories
                4. Competition levels
                5. Market opportunities
                Format as JSON with keys: trends, market_sentiment, opportunities, competition
                """,
                'products': f"""
                Discover trending products in {market}.
                Include:
                1. Top trending products with growth rates
                2. Product categories
                3. Target audience
                4. Price points
                5. Available affiliate programs
                Format as JSON with keys: trending_products, categories, affiliate_programs, metrics
                """,
                'seasonal': f"""
                Analyze seasonal trends for {market}.
                Include:
                1. Upcoming seasonal opportunities
                2. Seasonal products
                3. Timing recommendations
                4. Historical patterns
                5. Marketing suggestions
                Format as JSON with keys: seasons, opportunities, products, timing
                """,
                'affiliate': f"""
                Find affiliate programs in {market}.
                Include:
                1. Top programs
                2. Commission rates
                3. Program requirements
                4. Product categories
                5. Program ratings
                Format as JSON with keys: programs, commissions, requirements, products
                """
            }

            response = await model.generate_content_async(prompts[trend_type])
            return json.loads(response.text)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def analyze_competitor(url: str, analysis_type: str) -> Dict:
        try:
            prompts = {
                'strategy': f"""
                Analyze the affiliate marketing strategy for: {url}
                Include:
                1. Content strategy
                2. Traffic sources
                3. Monetization methods
                4. Unique selling points
                5. Areas for improvement
                Format as JSON with keys: strategy, traffic, monetization, strengths, improvements
                """,
                'keywords': f"""
                Analyze the keyword strategy for: {url}
                Include:
                1. Main keywords
                2. Content topics
                3. Search intent
                4. Keyword gaps
                5. Optimization suggestions
                Format as JSON with keys: keywords, topics, intent, gaps, suggestions
                """,
                'backlinks': f"""
                Analyze the backlink profile for: {url}
                Include:
                1. Link building strategies
                2. Authority metrics
                3. Link types
                4. Competitor comparisons
                5. Improvement opportunities
                Format as JSON with keys: strategies, metrics, types, comparison, opportunities
                """
            }

            response = await model.generate_content_async(prompts[analysis_type])
            return json.loads(response.text)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# API Endpoints
@router.post("/generate-content")
async def generate_content_endpoint(prompt: str, content_type: str):
    return await AIService.generate_content(prompt, content_type)

@router.post("/optimize-link")
async def optimize_link_endpoint(url: str, optimization_type: str):
    return await AIService.optimize_link(url, optimization_type)

@router.post("/analyze-audience")
async def analyze_audience_endpoint(niche: str, analysis_type: str):
    return await AIService.analyze_audience(niche, analysis_type)

@router.post("/analyze-trends")
async def analyze_trends_endpoint(market: str, trend_type: str):
    return await AIService.analyze_trends(market, trend_type)

@router.post("/analyze-competitor")
async def analyze_competitor_endpoint(url: str, analysis_type: str):
    return await AIService.analyze_competitor(url, analysis_type)
