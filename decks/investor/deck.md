---
marp: true
theme: comics-factory
paginate: true
header: AI StoryBook Pitch Deck
footer: © 2026 AI StoryBook
---

<!-- _class: title -->

![logo w:150](../assets/logo.svg)

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

{% for demo in product.demo %}
<!-- _class: demo -->

### {{ demo.title }}

<div class="columns">
<div class="column">

**Input**

<div class="demo-input">

*Text:* "{{ demo.input_text }}"

*Reference Image:*

![w:300]({{ demo.input_image }})

</div>
</div>

<div class="column">

**Generated Output**

![w:550]({{ demo.output_image }})

</div>
</div>

---

{% endfor %}

## Market Opportunity

<div class="emphasis">

- **TAM:** {{ product.market.tam }}
- **SAM:** {{ product.market.sam }}  
- **SOM:** {{ product.market.som }}

</div>

---

## Business Model

{% for item in product.business_model %}
- {{ item }}
{% endfor %}

---

## Roadmap

<div class="columns">
<div class="column">

### 🎯 Short Term
{{ product.roadmap.short_term }}

</div>

<div class="column">

### 🚀 Long Term
{{ product.roadmap.long_term }}

</div>
</div>

---

## Meet the Team

{% for member in product.team %}
<div class="emphasis">

**{{ member.name }}** - *{{ member.role }}*
{{ member.background }}

</div>
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

![logo w:120](../assets/logo.svg)
