<template>
    <v-expansion-panel>
        <v-expansion-panel-content>
            <template v-slot:header>
                <div>Markdown Help</div>
            </template>
            <Editor v-model="text" />
        </v-expansion-panel-content>
    </v-expansion-panel>
</template>

<script>
    import {
        Editor,
        Renderer,
        Toolbar
    } from 'vuetify-markdown-editor';

    // CSS for Editor
    import 'vuetify-markdown-editor/dist/vuetify-markdown-editor.css';

    /* Editor is a Vue component
     * Renderer is the internal rendering function
     * Toolbar is a Vue component used for some WYSIWYG functions
     */

    export default {
        components: {
            Editor
        },
        data() {
            return {
                text: `
Basic Elements
H1 to H6
Headings
# Heading Text
## Heading Text
### Heading Text
#### Heading Text
##### Heading Text
###### Heading Text
Italics	*This text is italicized*
Bold	**This text is bold**
Blockquote	> Blockquote paragraphs must have
> a right-arrow bracket at the start
> of every single line.
>
> Use a blank line for multiple paragraphs.
Unordered List	- Bullet list item
- Bullet list item
- Bullet list item
  - Use a two-space indent for nested lists
Ordered List	1. Bullet list item
2. Bullet list item
3. Bullet list item
  1. Ordered lists can also be nested
Mixed List	1. Can you mix list types?
  - Yes, you can!
Horizontal Line	---
***
___

Note: Either three hyphens, asterisks, or underscores.
Hyperlink	This is an [example link](//www.makeuseof.com)
Image	![Alt Text](http://example.com/image/path.png)
Ignore Markdown	Prefix Markdown characters with \*backslashes\* to ignore formatting.

Extended Elements

Strikethrough	~~This text is crossed out~~
Hard Line Break	This is some text\
This text is a new line, not a new paragraph
Table
| First Header | Second Header |
| ------------ | ------------- |
| Content cell 1 | Content cell 2 |
| Content column 1 | Content column 2 |

Note: Preceding blank line is necessary.
Task Lists	- [x] Completed task item
- [ ] Unfinished task item
- [ ] \(Optional) Mark parentheses to be ignored
Mention	You can mention @users and @teams on GitHub. Mainly useful when submitting or commenting on bugs and issues.
Emoji	:emojicode:

Note: Emoji codes can be found in the emoji cheat sheet.`,
            };
        }
    };
</script>