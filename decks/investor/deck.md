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

{{ product.subtitle }}

<p style="font-size: 0.9em; margin-top: 20px;">{{ product.mvp_status }}</p>

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

<div style="text-align: center; margin-top: 30px;">
<img src="../assets/qr_demo.png" width="180" />
<p style="font-size: 0.8em; color: #999; margin-top: 8px;">Scan for demo samples</p>
</div>

---

## Product Features

{% for item in product.features %}
- {{ item }}
{% endfor %}

---

## Innovation: Why We Win

{% for item in product.innovation %}
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

**Initial focus:** {{ product.market.initial_focus }}

</div>

---

## Business Model & Pricing

{% for item in product.business_model %}
- {{ item }}
{% endfor %}

---

## Technology & Scalability

{% for item in product.tech %}
- {{ item }}
{% endfor %}

---

## Go-To-Market Strategy

{% for item in product.gtm %}
- {{ item }}
{% endfor %}

---

## Competition & Differentiation

<div style="font-size: 0.85em;">

| Solution | Time | Consistency | Styles | Bulk |
|----------|------|-------------|--------|------|
{% for comp in product.competition.comparison_table.competitors %}
| **{{ comp.name }}** | {{ comp.time }} | {{ comp.consistency }} | {{ comp.styles }} | {{ comp.bulk }} |
{% endfor %}

**Key Differentiators:**
{% for diff in product.competition.differentiators %}
- {{ diff }}
{% endfor %}

</div>

---

## Roadmap

<div class="columns">
<div class="column">

### 🎯 Short Term (0–6 mo)
{{ product.roadmap.short_term }}

</div>

<div class="column">

### 🚀 Long Term (6–24 mo)
{{ product.roadmap.long_term }}

</div>
</div>

**Projected Outcomes:**
- Year 1: {{ product.roadmap.outcomes.y1 }}
- Year 2: {{ product.roadmap.outcomes.y2 }}
- Year 3: {{ product.roadmap.outcomes.y3 }}

---

## Traction

{% for item in product.traction %}
- {{ item }}
{% endfor %}

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
