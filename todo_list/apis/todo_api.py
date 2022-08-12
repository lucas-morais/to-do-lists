from ninja import Router
from django.shortcuts import get_object_or_404
from ..schemas.todo_schema import TodoDTO, TodoForm, TodoUpdateForm
from ..models.todo_models import Todo
from typing import List

router = Router()


@router.get("", response=List[TodoDTO])
def list_all(_request):
    todos = Todo.objects.all()
    return todos


@router.post("", response=TodoDTO)
def create_todo(_request, todo_form: TodoForm):
    todo = Todo(**todo_form.dict())
    todo.save()
    return todo


@router.get("/{str:id}", response=TodoDTO)
def list_by_id(_request, id: str):
    todo = get_object_or_404(Todo, id=id)
    return todo


@router.put("/{str:id}", response=TodoDTO)
def update(_request, id: str, updateForm: TodoUpdateForm):
    todo = get_object_or_404(Todo, id=id)
    todo.category = updateForm.category
    todo.description = updateForm.description
    todo.finished = updateForm.finished
    todo.save()
    return todo
