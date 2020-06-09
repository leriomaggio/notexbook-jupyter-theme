{%- extends 'full.tpl' -%}

{%- block html_head -%}
{{ super() }}
<style type="text/css">
  div.output_prompt {
    line-height: 0;
    font-size:0;
    color: transparent;
    left: -10000px;
    content: "\21E2";
    min-width: 33px;
  }

  @media (min-width: 1400px) {
  .container {
      width: 1350px;
  }
}
</style>
{%- endblock html_head -%}