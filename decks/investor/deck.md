---
marp: true
theme: comics-factory
paginate: true
header: Comics Factory Pitch Deck
footer: © 2026 Comics Factory
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

<div class="columns" style="align-items: center;">
<div class="column">

**Input**

<div class="demo-input" style="font-size: 0.85em;">

*Plot:* "{{ demo.input_text }}"

*Reference Image:*

![w:220](../{{ demo.input_image }})

</div>
</div>

<div class="column">

**Generated Output**

{% if demo.output_images %}
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 5px; max-width: 320px; max-height: 280px;">
{% for img in demo.output_images %}
<img src="../{{ img }}" style="width: 100%; height: 100%; object-fit: contain; border-radius: 4px;" />
{% endfor %}
</div>
{% else %}
![w:320](../{{ demo.output_image }})
{% endif %}

{% if demo.output_note %}
<p style="font-size: 0.7em; color: #999; margin-top: 6px;">{{ demo.output_note }}</p>
{% endif %}

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
