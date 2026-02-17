---
marp: true
theme: custom
paginate: true
header: AI StoryBook Pitch Deck
footer: © 2026 AI StoryBook
---

<!-- _class: title -->

# {{ product.name }}
## {{ product.tagline }}

---

## The Problem

{% for item in product.problem %}
- {{ item }}
{% endfor %}

---

## Our Solution

{% for item in product.solution %}
- {{ item }}
{% endfor %}

---

## Market Opportunity

- **TAM:** {{ product.market.tam }}
- **SAM:** {{ product.market.sam }}
- **SOM:** {{ product.market.som }}

---

## Business Model

{% for item in product.business_model %}
- {{ item }}
{% endfor %}

---

## Roadmap

### Short Term
{{ product.roadmap.short_term }}

### Long Term
{{ product.roadmap.long_term }}

---

## Meet the Team

{% for member in product.team %}
### {{ member.name }} - {{ member.role }}
{{ member.background }}

{% endfor %}

---

## The Ask

<div class="highlight">
{{ product.ask }}
</div>

---

<!-- _class: title -->

# Thank You!
## Let's build the future of storytelling together.
