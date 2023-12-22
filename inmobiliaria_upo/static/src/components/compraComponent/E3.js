/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class E3Componente extends Component {
    setup() {
        this.state = useState({
            task:{mensualidades:"1", amount_total:"0"},
            taskList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "inmobiliaria_upo.compra"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["mensualidades", "amount_total"])
    }

    async saveTask(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }

        await this.getAllTasks()
    }

    resetForm(){
        this.state.task = {mensualidades:"1", amount_total:"0"}
    }
 
}
    
E3Componente.template = 'owl.E3Componente';
registry.category('actions').add('owl.action_E3Componente_js', E3Componente);